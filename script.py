striped_data = []
extracted_data = []
bangla_digits = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯']
with open('voter_data.txt', 'r', encoding='utf8') as f:
    for line in f:
        line_data = line.strip()
        if len(line_data):
            # print(line_data[:4])
            striped_data.append(line_data)
print(striped_data)
current_serial_index = 0
previous_serial_index = 0
for idx, line in enumerate(striped_data):  # 1, 2n data
    # serial_no = line_data[:4]
    serial_no = line[:1]
    for a in serial_no:  # a= 0
        if a in bangla_digits:  # True
            if current_serial_index != idx:
                previous_serial_index, current_serial_index = current_serial_index, idx
                extracted_data.append(
                    striped_data[previous_serial_index:current_serial_index])
            print("Correct")
    if idx == len(striped_data)-1:
        extracted_data.append(striped_data[current_serial_index:idx])
print(extracted_data)
