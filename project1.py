import re
import csv
def main():
    with open('files/input.txt', 'r') as inputfile:
        emails = []
        for line in inputfile:
            if re.search('^From:',line):
                email = line.rstrip().split()[1]
                print(email)
                emails.append(email)

        emaildict = {}
        for email in emails:
            emaildict[email] = emaildict.get(email,0) + 1
        print(f'{emaildict}')

    #list = emaildict.items()
    field_names = ['Email', 'Count']
    with open('output.csv', 'w') as outputfile_csv:
        content = csv.writer(outputfile_csv)
        content.writerow(field_names)
        total = 0
        for key, value in emaildict.items():
            content.writerow([key,value])
            total = total + value
        content.writerow(['Total',total])

    with open('files/output.txt', 'w') as outputfile:
        total = 0
        with open('files/input.txt', 'r') as inputfile:
            for line in inputfile:
                if re.search('^X-DSPAM-Confidence:',line):
                    outputfile.write(line)
                    total += float(line.split()[1])
            print(total)
            outputfile.write(f'Total dspam confidence = {total:.2f}')





if __name__ == '__main__':
    main()