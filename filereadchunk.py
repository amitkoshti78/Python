def read_records_in_batches_buffer(file_name, batch_size=10):
    with open(file_name, 'r') as file:
        while True:
            lines = []
            for _ in range(batch_size):
                line = file.readline().strip()
                if not line:
                    break
                lines.append(line)
            
            if not lines:
                break  # No more lines to process

            # Process the current batch
            print(f"Processing {len(lines)} records...")
            for line in lines:
                print(line)

            print("\n--- End of Batch ---\n")


file_name = 'records.txt'
read_records_in_batches_buffer(file_name)
