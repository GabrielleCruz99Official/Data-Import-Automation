resource "aws_s3_bucket" "csv_bucket" {
  bucket = "${var.project}-${var.env}-s3-csv-bucket"

  tags = {
    Name        = "CSV"
    Environment = var.env
  }

  force_destroy = true
}

resource "aws_lambda_permission" "allow_bucket" {
  statement_id = "AllowExecutionFromS3Bucket"
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.inbound.arn
  principal = "s3.amazonaws.com"
  source_arn = aws_s3_bucket.csv_bucket.arn
}

resource "aws_iam_role_policy_attachment" "lambda_s3"{
  role = aws_iam_role.migration_role.name
  policy_arn = aws_iam_policy.lambda_s3_pol.arn
}

resource "aws_s3_bucket_notification" "aws_inbound_lambda_trigger" {
  bucket = aws_s3_bucket.csv_bucket.id
  lambda_function {
    lambda_function_arn = aws_lambda_function.inbound.arn
    events = ["s3:ObjectCreated:*"]
    filter_prefix = "Out/"
  }
  depends_on = [aws_lambda_permission.allow_bucket]
}