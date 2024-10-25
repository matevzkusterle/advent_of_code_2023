import re

vsota_id = 0
with open(file="file2.txt", mode="r") as f:
    for line in f:
        game_number_match = re.search(r'Game\s+(\d+):', line)
        if game_number_match:
            game_number = int(game_number_match.group(1))
        
        # Split the line by ';' to get each set of numbers
        segments = line.split(';')
        
        all_segments_valid = True
        
        for segment in segments:
            red = 0
            blue = 0
            green = 0
            
            # Find all matches for numbers followed by a color
            matches = re.findall(r'(\d+)\s+(red|blue|green)', segment)
            
            # Sum the numbers based on their color
            for match in matches:
                number, color = int(match[0]), match[1]
                if color == 'red':
                    red += number
                elif color == 'blue':
                    blue += number
                elif color == 'green':
                    green += number

            # Check the condition for the current segment
            if not (red <= 12 and blue <= 14 and green <= 13):
                all_segments_valid = False
                break
        
        if all_segments_valid:
            vsota_id += game_number

print(vsota_id)



#da pozenemo gremo v terminalu v ta file in napisemo python 2.py