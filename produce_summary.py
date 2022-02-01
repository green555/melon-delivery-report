def melon_sale_summary(file_name):
    the_day = file_name[-9:-4]
    print(the_day)
    the_file = open(file_name)

    for line in the_file:

        line = line.rstrip()
        words = line.split('|')
        melon, count, amount = words

        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()

melon_sale_summary("um-deliveries-day-1.txt")
melon_sale_summary("um-deliveries-day-2.txt")
melon_sale_summary("um-deliveries-day-3.txt")
