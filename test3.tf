provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "vulnerable_bucket" {
  bucket = "my-public-bucket-demo"
  acl    = "public-read"  # ❌ Publicly readable bucket

  versioning {
    enabled = false  # ❌ No versioning — risk of accidental data loss
  }

  logging {
    target_bucket = ""
    target_prefix = "log/"  # ❌ No logging target
  }

  tags = {
    Name = "UnsecureBucket"
    Environment = "dev"
  }
}

resource "aws_security_group" "open_sg" {
  name        = "open-sg"
  description = "Security group with wide open ingress"
  vpc_id      = "vpc-123456"

  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # ❌ Wide open to the internet
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
