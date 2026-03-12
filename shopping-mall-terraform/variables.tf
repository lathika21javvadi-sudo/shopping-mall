variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
}

variable "availability_zone" {
  description = "Availability zone for EC2"
  type        = string
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

variable "key_name" {
  description = "Name of the EC2 key pair"
  type        = string
}

variable "ami_id" {
  description = "AMI ID for EC2 instance"
  type        = string
}