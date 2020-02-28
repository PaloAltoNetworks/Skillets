variable "access_key" {
    description = "AWS Access Key"
    default = ""
}
variable "secret_key" {
    description = "AWS Secret Key"
    default = ""
}

# AWS Region and Availablility Zone
variable "region" {
    default = "us-east-1"
}