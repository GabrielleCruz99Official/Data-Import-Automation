data "archive_file" "inbound_zip"{
    type = "zip"
    source_dir = "${path.module}/../workers/inbound"
    output_path = "${path.module}/../workers/inbound/inbound.zip"
    excludes = fileset("../workers/inbound/", "*.zip")
}

data "archive_file" "outbound_zip"{
    type = "zip"
    source_dir = "${path.module}/../workers/outbound"
    output_path = "${path.module}/../workers/outbound/outbound.zip"
    excludes = fileset("../workers/outbound/", "*.zip")
}