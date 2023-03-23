resource "aws_lambda_function" "inbound" {
  #s3_bucket     = var.s3_bucket
  #s3_key        = var.s3_key_inbound
  filename = data.archive_file.inbound_zip.output_path
  source_code_hash = data.archive_file.inbound_zip.output_base64sha256
  function_name = "${var.project}-${var.env}-inbound"
  role = aws_iam_role.migration_role.arn
  handler = var.handler_inbound
  runtime = var.runtime
  timeout     = 900
  memory_size = 1024
  depends_on = [
    aws_iam_role_policy_attachment.lambda_logs
  ]
  environment {
    variables = {
      SQS_URL = aws_sqs_queue.data_migration_queue.id
      FUNCTION_DEBUG_LEVEL = var.function_debug_level
    }
  }

}

resource "aws_cloudwatch_log_group" "function_log_group_inbound" {
  name              = "/aws/lambda/${aws_lambda_function.inbound.function_name}"
  retention_in_days = 30
  lifecycle {
    prevent_destroy = false
  }
}