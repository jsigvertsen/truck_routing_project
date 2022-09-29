class Hash:
    # Cited:
    # Dr. Cemal Tepe. (2020, November 17). C950 - Webinar-1 - Let's Go Hashing [Video].
    # Western Governor's University.
    # https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=f08d7871-d57a-496e-a6a1-ac7601308c71
    def __init__(self, length=40):  # set the length to 40 unless otherwise specified
        self.lst = []
        for i in range(length):
            self.lst.append([])  # empty bucket locations are added

    def insert(self, key, item):
        # the list is recreated every time this method is used
        bucket = hash(key) % len(self.lst)  # create the bucket where the data is stored
        bucket_list = self.lst[bucket]  # assign the bucket to a point in the list
        for i in bucket_list:  # search the list of buckets for a matching key
            if i[0] == key:  # if the key matches an existing key, update the item data
                i[1] = item
                return True
        key_value = [key, item]  # create a key, item pair
        bucket_list.append(key_value)  # append the pair to the list
        return True

    def search(self, key):
        # the list is recreated every time this method is used
        bucket = hash(key) % len(self.lst)  # create the bucket where the data is stored
        bucket_list = self.lst[bucket]  # assign the bucket to a point in the list

        for i in bucket_list:
            if i[0] == key:  # if a key matches, return the item data
                return i[1]
        return None

    def remove(self, key):
        # the list is recreated every time this method is used
        bucket = hash(key) % len(self.lst)  # create the bucket where the data is stored
        bucket_list = self.lst[bucket]  # assign the bucket to a point in the list

        for i in bucket_list:
            if i[0] == key:  # if the key matches, remove the key and item data from the list
                bucket_list.remove([i[0], i[1]])
