class Video:
    """
    Parameters:
  - video_id: The ID of the video.
  - title: The title of the video.
  - description: The description of the video
  - time: The duration of the video in seconds
    """
    # your code here:
    def __init__(self):
        self.video_id = None
        self.title = None
        self.description = None
        self.time = None

    def addInfo(self):
        self.video_id = input("Enter id: ")
        self.title = input("Enter title: ")
        self.description = input("Enter description: ")
        self.time = input("Enter time: ")

    def showInfo(self):
        print(f"ID: {self.video_id} - Title: {self.title} - Description: {self.description} - Time: {self.time}")

# Node is an element of the TikTokPlaylist (use Doubly Linked List structure)
class Node:
    # your code here:
    def __init__(self, value: Video):
        self.value = value
        self.next = None
        self.prev = None

# DO NOT change method name.
class TikTokPlaylist:
    # your code here
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __checkID(self, video_id):
        temp = self.head
        while temp is not None:
            if temp.value.video_id == video_id:
                return True
            temp = temp.next
        return False

    def add_video(self, video):
        """
        Add the video to the list's tail (duplicate video_id is not allowed)
        :param video: Video object
        :return: void
        """
        # your code here
        video_id = video.video_id
        newNode = Node(video)
        if self.__checkID(video_id):
            print("Duplicate video_id is not allowed!!!")
        else:
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            else:
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            self.size += 1

    def remove_video(self, video_id):
        """
        Remove and return the video by video_id.
        :param video_id: the ID of the video to be removed
        :return: Video object (the video that has been deleted) or None if not found
        """
        # your code here
        temp = self.head
        if self.head.value.video_id == video_id:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail.value.video_id == video_id:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            while temp is not None and temp.value.video_id != video_id:
                temp = temp.next
            if temp is None:
                print("Video is not in list!!!")
            else:
                prev = temp.prev
                prev.next = temp.next
                temp.next = None
                temp.prev = None
        self.size -= 1

    def display_videos(self):
        """
        Prints the content of all videos in the list, starting from head.
        :return: void
        """
        # your code here
        temp = self.head
        while temp is not None:
            temp.value.showInfo()
            temp = temp.next


    def search_videos(self, keyword):
        """
        Traverse and return all videos that have keyword in their title.
        :param keyword: the keyword to search for in video titles
        :return: list of videos that contain the keyword in their title, [] otherwise
        """
        # your code here
        result = []
        temp = self.head
        while temp is not None:
            if keyword in temp.value.title:
                result.append(temp.value)
                temp.value.showInfo()
            temp = temp.next
        return result


    def remove_video_by_keyword(self, keyword):
        """
        Remove all videos that have the keyword in their title or description.
        :param keyword: the keyword to search for in video titles or descriptions
        :return: void
        """
        # your code here
        list_videos = []
        temp = self.head
        while temp.next is not None:
            if keyword not in temp.value.title or keyword not in temp.value.description:
                list_videos.append(temp.value)
            temp = temp.next
        self.head = None
        self.tail = None
        for i in range(len(list_videos)):
            self.add_video(list_videos[i])

    def shuffle_videos(self):
        import random
        """
        Shuffle the order of videos in the playlist.
        :return: void
        """
        # your code here
        list_video = []
        temp = self.head
        while temp is not None:
            list_video.append(temp.value)
            temp = temp.next
        random.shuffle(list_video)
        self.head = None
        self.tail = None
        for i in range(len(list_video)):
            self.add_video(list_video[i])


# your code to create menu
def menu():
    print("""
        0. Exit
        1. Add video
        2. Remove video
        3. Display videos
        4. Search videos by keyword
        5. Remove videos by keyword
        6. Shuffle video list
    """)

# your code here to test
playlist = TikTokPlaylist()
while True:
    menu()
    option = int(input("Choose option: "))
    if option == 0:
        break
    elif option == 1:
        newVideo = Video()
        newVideo.addInfo()
        playlist.add_video(newVideo)
    elif option == 2:
        video_id = input("Enter video id to remove: ")
        playlist.remove_video(video_id)
    elif option == 3:
        playlist.display_videos()
    elif option == 4:
        keyword = input("Enter keyword to search: ")
        playlist.search_videos(keyword)
    elif option == 5:
        keyword = input("Enter keyword to remove: ")
        playlist.remove_video_by_keyword(keyword)
    elif option == 6:
        playlist.shuffle_videos()