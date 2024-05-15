from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            # Move the accessed key to the end
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            # Move the accessed key to the end
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # Remove the least recently used item (first item in OrderedDict)
            self.cache.popitem(last=False)
        self.cache[key] = value

# Example usage:
if __name__ == "__main__":
    capacity = int(input("Enter the capacity of the page table: "))
    page_references = list(map(int, input("Enter the page references separated by spaces: ").split()))

    lru_cache = LRUCache(capacity)
    page_faults = 0

    for page in page_references:
        if lru_cache.get(page) == -1:
            lru_cache.put(page, True)
            page_faults += 1

    print("Total Page Faults:", page_faults)
