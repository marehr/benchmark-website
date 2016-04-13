
# handle uploaded json file
def handle_uploaded_file(f):
    with open('/home/mi/marehr/ClionProjects/benchmark_project/benchmark_app/test.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def create_compare_json_file(benchmark_ids):
    return {"key": "value"}
