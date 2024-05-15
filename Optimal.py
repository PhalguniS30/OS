def optimalPageFaults(pages, capacity):
    page_faults = 0
    page_table = []
    future_pages = pages.copy()

    for i in range(len(pages)):
        if pages[i] not in page_table:
            if len(page_table) < capacity:
                page_table.append(pages[i])
            else:
                page_to_replace = -1
                farthest_used_index = -1
                for page in page_table:
                    if page not in future_pages[i:]:
                        page_to_replace = page
                        break
                    else:
                        index = future_pages[i:].index(page)
                        if index > farthest_used_index:
                            farthest_used_index = index
                            page_to_replace = page
                page_table[page_table.index(page_to_replace)] = pages[i]
            page_faults += 1
        future_pages.remove(pages[i])
    return page_faults


if __name__ == '__main__':
    capacity = int(input("Enter the capacity of the page table: "))
    pages = list(map(int, input("Enter the page references separated by spaces: ").split()))
    print("Total Page Faults:", optimalPageFaults(pages, capacity))
