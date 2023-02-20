variable "region" {
  default = "us-east-1"
  type    = string
}

variable "env" {
  default = "dev"
  type    = string
}

variable "project" {
  default = "data-migration"
  type    = string
}

variable "instance_name" {
  description = "Value of the Name tag for the EC2 instance"
  type        = string
  default     = "DataImportAutomation"
}