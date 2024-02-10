# Place code below to do the munging part of this assignment.
original_data_filename = 'data/GLB.Ts+dSST.txt'
munged_data_filename = 'data/clean_data.csv'
heading_string = 'Year   Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov  Dec    J-D D-N    DJF  MAM  JJA  SON  Year'


def celcius_to_farenheit_diff(celcius):
    return celcius * 9/5

def readlines(filename):
    with open(filename) as f:
        return f.readlines()
    
def clean_data(lines):
    cleaned_lines = []
    for line in lines:
        try :
            int(line.split()[0])
            cleaned_lines.append(line)
        except ValueError:
            pass
        except IndexError:
            pass
    return cleaned_lines

def write_to_file(filename, lines):
    headings = heading_string.split()[:-1]
    heading_csv = ','.join(headings)
    with open(filename, 'w') as f:
        f.write(heading_csv + '\n')
        for line in lines:
            raw_data = line.split()[:-1]
            for i in range(1, len(raw_data)):
                try:
                    float(raw_data[i])
                except ValueError:
                    raw_data[i] = 'NaN'
                farenheit = celcius_to_farenheit_diff(float(raw_data[i])/100)
                raw_data[i] = format(farenheit, '.1f')
            f.write(','.join(raw_data) + '\n')


if __name__ == '__main__':
    lines = readlines(original_data_filename)
    cleaned_lines = clean_data(lines)
    write_to_file(munged_data_filename, cleaned_lines)
    print('Data munged and written to file')

        
