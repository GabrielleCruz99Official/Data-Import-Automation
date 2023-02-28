resource "aws_sqs_queue" "data_migration_queue" {
    name                        = "${var.project}-${var.env}-migration"
    message_retention_seconds   = 86400
    receive_wait_time_seconds   = 10
    visibility_timeout_seconds  = 300
    content_based_deduplication = false
    redrive_policy              = "{\"deadLetterTargetArn\":\"${aws_sqs_queue.data_migration_deadletter_queue.arn}\",\"maxReceiveCount\":4}"
}

resource "aws_sqs_queue" "data_migration_deadletter_queue" {
    name                        = "${var.project}-${var.env}-DLQ-migration"
    message_retention_seconds   = 86400
    receive_wait_time_seconds   = 10
    visibility_timeout_seconds  = 300
    content_based_deduplication = false
}

resource "aws_iam_role_policy_attachment" "lambda_sqs" {
    role       = aws_iam_role.migration_role.name
    policy_arn = aws_iam_policy.lambda_sqs_pol.arn
}