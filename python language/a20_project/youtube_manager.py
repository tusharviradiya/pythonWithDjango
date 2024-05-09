import json

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            test = json.load(file)
            # print(test)
            return test
    except FileNotFoundError:
        return []
    # finally:
    #     pass

def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*"*50)
    print("\n")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['title']}, Duration: {video['time']}")
    print("\n")
    print("*"*50)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"title": name, "time": time})
    save_data_helper(videos)

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video index for delete video "))
    if 1 <= index <= len(videos):
        # videos.pop(index - 1)
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("invalid index")

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video index for update video "))
    if 1 <= index <= len(videos):
        name = input("Enter video name: ")
        if name == "" or time == "":
            return
        time = input("Enter video time: ")
        videos[index - 1] = {"title": name, "time": time}
        save_data_helper(videos)
    else:
        print("invalid index")


def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | chose any option")
        print("1. list all videos")
        print("2. Add video")
        print("3. Delete video")
        print("4. Update video")
        print("5. Exit")
        choice = int(input())
        # print(videos)

        match choice:
            case 1:
                list_all_videos(videos)
            case 2:
                add_video(videos)
            case 3:
                delete_video(videos)
            case 4:
                update_video(videos)
            case 5:
                break
            case _:
                print("invalid choice")

if __name__ == "__main__":
    main()