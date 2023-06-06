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

variable "bump_version" {
  type        = string
  description = "Function version"
  default     = false
}

variable "handler_inbound" {
  type        = string
  description = "Handler for calling serverless function"
  default     = "inbound.process_event"
}

variable "handler_outbound" {
  type        = string
  description = "Handler for calling serverless function"
  default     = "outbound.process_event"
}

variable "runtime" {
  type        = string
  description = "The handler runtime version for serverless invocation"
  default     = "python3.8"
}

variable "s3_bucket" {
  type        = string
  description = "The S3 bucket that holds the packaged function"
}

variable "s3_key_inbound" {
  type        = string
  description = "The default key for zip artifact on s3 bucket"
  default     = "default-artifact"
}

variable "s3_key_outbound" {
  type        = string
  description = "The default key for zip artifact on s3 bucket"
  default     = "default-artifact"
}

variable "s3_key_destination_layer" {
  type        = string
  description = "The default key for zip artifact on s3"
  default     = "default-artifact"
}

variable "instance_name" {
  description = "Value of the Name tag for the EC2 instance"
  type        = string
  default     = "DataImportAutomation"
}

variable "function_debug_level" {
  type        = string
  description = "Debug level of the lambdas"
  default     = "DEBUG"
}