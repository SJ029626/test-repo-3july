provider "aws" {
  region = "us-east-1"
}

# ❌ Public S3 bucket with no logging or encryption
resource "aws_s3_bucket" "public_bucket" {
  bucket = "example-insecure-bucket"
  acl    = "public-read"  # Exposes bucket contents publicly

  versioning {
    enabled = false  # ❌ No versioning — risk of data loss
  }

  server_side_encryption_configuration {
    # ❌ Missing encryption block entirely
  }

  tags = {
    Environment = "dev"
    Team        = "infrastructure"
  }
}

# ❌ Security group open to the world
resource "aws_security_group" "open_sg" {
  name        = "open-sg"
  description = "Open ingress to all traffic"
  vpc_id      = "vpc-xxxxxxx"

  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # ❌ Wide open access
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# ❌ EC2 instance with plaintext credentials and SSH open
resource "aws_instance" "insecure_instance" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tag
