def read_file_in_chunks(file_name, chunk_size=3):
    with open(file_name, "r") as file:
        while True:
            lines = []
            
            for _ in range(chunk_size):
                line = file.readline().strip()
                
                if not line:
                    continue
                else:
                    lines.append(line)
        
            if not lines:
                break
            
            print("\n#### Printing lines in chunk ####")
            for record in lines:
                print(record)
            print("\n!!! End of Chunk !!!")

def update_file(file_name, old_record, new_record):
    
    with open(file_name, "r") as file_rd:
        lines = file_rd.readlines()
        print(lines)
        
    with open(file_name, "w") as file_wr:
        found = False
        for old_line in lines:
            if old_line.strip() == old_record.strip():
               
                found = True
                file_wr.write(new_record + "\n")
            else:
                file_wr.write(old_line)

        if found:
             print("record found")
        else:
             print("record not found")
                

if __name__ == "__main__" :
    filename = "records.txt"  
    read_file_in_chunks(filename)
    old_record = "Akshay;Patil;Akshay.Patil@yahoo.com;9270022736" 
    new_record = "Akshay;Patil;Akshay.Patil@gmail.com;9150021725"
    update_file(filename, old_record, new_record)
    
    