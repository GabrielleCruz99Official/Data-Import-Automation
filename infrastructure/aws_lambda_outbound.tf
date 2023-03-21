resource "aws_lambda_function" "outbound" {
    #s3_bucket = var.s3_bucket
    #s3_key = var.s3_key_outbound
    filename = data.archive_file.outbound_zip.output_path
    function_name = "${var.project}-${var.env}-outbound"
    role = aws_iam_role.migration_role.arn
    publish = true
    handler = var.handler_outbound
    runtime = var.runtime
    timeout = 300
    #layers = [aws_lambda_layer_version.lambda_layer_data_migration.arn]
    depends_on = [
        aws_iam_role_policy_attachment.lambda_logs
    ]
    dead_letter_config {
        target_arn = aws_sqs_queue.data_migration_deadletter_queue.arn
    }
    environment {
        variables = {
            DLQ_SQS_URL = aws_sqs_queue.data_migration_deadletter_queue.id
            SEGMENT_WRITE_KEY = var.segment_write_key
            FUNCTION_DEBUG_LEVEL = var.function_debug_level
        }
    }
}

resource "aws_cloudwatch_log_group" "function_log_group_outbound" {
    name = "/aws/lambda/${aws_lambda_function.outbound.function_name}"
    retention_in_days = 30
    lifecycle {
        prevent_destroy = false
    }
}

resource "aws_lambda_event_source_mapping" "outbound_event_source_mapping" {
    event_source_arn = aws_sqs_queue.data_migration_queue.arn
    enabled = true
    function_name = aws_lambda_function.outbound.qualified_arn
    batch_size = 100
    maximum_batching_window_in_seconds = 10
    depends_on = [aws_lambda_function.outbound, aws_sqs_queue.data_migration_queue]
}