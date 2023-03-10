data "archive_file" "inbound_zip"{
    type = "zip"
    source_dir = "${path.module}/../workers/inbound"
    output_path = "${path.module}/../package/inbound.zip"
}

data "archive_file" "outbound_zip"{
    type = "zip"
    source_dir = "${path.module}/../workers/outbound"
    output_path = "${path.module}/../package/outbound.zip"
}