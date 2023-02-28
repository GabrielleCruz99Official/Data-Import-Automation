output "instance_id" {
  description = "EC2 instance ID"
  value       = aws_instance.app_server.id
}

output "instance_public_ip" {
  description = "Public IP address of EC2 instance"
  value       = aws_instance.app_server.public_ip
}

output "CSV_UPLOAD_TO_STAGING_COMMAND" {
  description = "Resource ARN"
  value       = "aws s3 cp <YOUR FILENAME>.csv s3://${aws_s3_bucket.csv_bucket.bucket}/In/<YOUR FILENAME>.csv"
}

output "CSV_LAUNCH_IMPORT_OF_STAGING_CSV_COMMAND" {
  description = "Resource ARN"
  value       = "aws s3 mv s3://${aws_s3_bucket.csv_bucket.bucket}/In/<YOUR FILENAME>.csv s3://${aws_s3_bucket.csv_bucket.bucket}/Out/<YOUR FILENAME>.csv"
}