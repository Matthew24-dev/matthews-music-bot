from collections import defaultdict

# Queue storage
QUEUE = defaultdict(list)


def add_to_queue(chat_id: int, song: dict):
    """
    Add a song to a group's queue.
    song = {
        "title": "...",
        "url": "...",
        "duration": "...",
        "requested_by": "..."
    }
    """
    QUEUE[chat_id].append(song)


def get_queue(chat_id: int):
    """Return the queue for a group."""
    return QUEUE.get(chat_id, [])


def pop_queue(chat_id: int):
    """Remove and return the first song in the queue."""
    if chat_id in QUEUE and QUEUE[chat_id]:
        return QUEUE[chat_id].pop(0)
    return None


def clear_queue(chat_id: int):
    """Clear the group's queue."""
    if chat_id in QUEUE:
        QUEUE[chat_id].clear()


def queue_size(chat_id: int):
    """Return the number of queued songs."""
    return len(QUEUE.get(chat_id, []))


def is_queue_empty(chat_id: int):
    """Check whether the queue is empty."""
    return queue_size(chat_id) == 0


def current_song(chat_id: int):
    """Return the current song without removing it."""
    if chat_id in QUEUE and QUEUE[chat_id]:
        return QUEUE[chat_id][0]
    return None