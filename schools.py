import csv

def load_data(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            school, score1, score2 = row
            data.append((school, score1, score2))
    return data

def find_schools(data, score):
    eligible_schools = []
    for school, score1, score2 in data:
        if int(score) >= int(score1) and int(score) >= int(score2):
            eligible_schools.append((school, score1, score2))
    return eligible_schools

def main():
    file_path = 'schools.csv'
    data = load_data(file_path)
    score = input("请输入您的报考分数：")
    eligible_schools = find_schools(data, score)
    
    if eligible_schools:
        print("您可以报考的学校有：")
        for school, min_score, max_score in eligible_schools:
            print(f"{school}（最低分：{min_score}，最高分：{max_score}）")
    else:
        print("您的分数不符合任何学校的要求，请继续努力！")
    input("Press enter to exit...")

if __name__ == "__main__":
    main()
