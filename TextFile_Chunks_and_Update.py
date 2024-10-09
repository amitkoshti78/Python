def read_file_in_chunks(file_name, chunk_size=3):

    try:
        with open (file_name, "r") as file_handle:
            while True:
                lines = []
                count = 0
                lines = [file_handle.readline().strip() for _ in range(chunk_size) ]
                print(lines)
                lines = [record for record in lines if record]
                print(lines)
                """ for _ in  range(chunk_size):
                    #lines = [line for line in lines if line]
                    line = file_handle.readline().strip()
                    if not line:
                        continue
                    else:
                        count +=1
                        lines.append(line)"""

                if not lines:
                    break

                print(f"\n #---- Processing Lines {count} --- #")

                for line in lines:
                    print(line)

                print("\n # !!! End of chunk !!! #")

    except FileNotFoundError:
        print(f"File {file_name} does not exists")
    finally:
        print('Function read_file_in_chunk ended')

def update_record_in_file(file_name, old_record, new_record):
    try:
        with open(file_name, "r" ) as file_rd:
            lines = file_rd.readlines()
           
    except FileNotFoundError:
        print(f"File {file_name} does not exists")
    finally:
        print('Function read_file_in_chunk ended')
        
    try:
        with open(file_name, "w") as file_wr:
            rec_updated = False
            for old_line in lines:
                if old_line.strip() == old_record.strip():
                    file_wr.write(new_record.strip() + "\n")
                    rec_updated = True
                else:
                    file_wr.write(old_line.strip() + "\n")
                    
    except Exception as err:
        print(f"File {file_name} error occurred while writing {err}")
    else:
        if rec_updated:
            print("Record updated successfully")
        else:
            print("Record not found")

    





if __name__ == '__main__':
    file_name = "records.txt"
    read_file_in_chunks(file_name)
    old_record = "Akshay;Patil;Akshay.Patil@gmail.com;9268001318"
    new_record = "Akshay;Patil;Akshay.Patil@yahoo.com;9157023737"
    update_record_in_file(file_name, old_record, new_record)
