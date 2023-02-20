resource "aws_s3_bucket" "csv_bucket" {
  bucket = "${var.project}-${var.env}-s3-csv-bucket"

  tags = {
    Name        = "CSV"
    Environment = var.env
  }

  force_destroy = true
}