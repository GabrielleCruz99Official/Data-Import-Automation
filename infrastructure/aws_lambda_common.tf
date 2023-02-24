resource "aws_iam_policy" "lambda_logging" {
  name        = "${var.project}-${var.env}-logging"
  path        = "/"
  description = "IAM policy for logging from lambdas"

  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "logs:CreateLogGroup"
            ],
            "Resource": "arn:aws:logs:*:*:*",
            "Effect": "Allow"
        }
    ]
}
EOF
}

resource "aws_iam_policy" "lambda_sqs_pol" {
  name        = "${var.project}-${var.env}-lambda_sqs_policy_tfe"
  path        = "/"
  description = "IAM policy for writing/reading SQS from a lambda"

  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "",
            "Effect": "Allow",
            "Action": "sqs:*",
            "Resource": "*"
        }
    ]
}
EOF
}

resource "aws_iam_policy" "lambda_s3_pol" {
  name        = "${var.project}-${var.env}-lambda_s3_policy"
  path        = "/"
  description = "IAM policy for writing/reading SQS from a lambda"

  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "",
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "*"
        }
    ]
}
EOF
}