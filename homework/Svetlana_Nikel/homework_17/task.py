import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('archive_path', help='Location of log archive directory')
parser.add_argument('-t', '--text', required=True, help='Pattern to identify')
args = parser.parse_args()


def scan_directory_contents(container: str):
    return [
        os.path.join(container, item)
        for item in os.listdir(container)
        if os.path.isfile(os.path.join(container, item))
    ]


def detect_pattern_in_record(record: str, target: str, record_number: int, document_name: str):
    findings = []
    elements = record.strip().split()

    if target in elements:
        location = elements.index(target)
        previous_elements = elements[max(0, location - 5): location]
        next_elements = elements[location + 1: location + 6]
        extracted_context = ' '.join(previous_elements) + f" {target} " + ' '.join(next_elements)
        findings.append((document_name, record_number, extracted_context))

    return findings


def examine_document(document_path: str, pattern: str):
    collected_data = []
    with open(document_path, 'r', encoding='utf-8', errors='ignore') as data_source:
        for counter, content_line in enumerate(data_source, start=1):
            located_items = detect_pattern_in_record(content_line, pattern, counter, os.path.basename(document_path))
            collected_data.extend(located_items)
    return collected_data


def process_log_collection():
    for data_file in scan_directory_contents(args.archive_path):
        examination_results = examine_document(data_file, args.text)
        for doc_name, line_num, context_block in examination_results:
            print(f'Document: {doc_name}, Position: {line_num}')
            print(context_block)


process_log_collection()
