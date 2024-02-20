import concurrent.futures


class ThreadPool:
    def __init__(self, num_threads):
        self.executor = concurrent.futures.ThreadPoolExecutor(
            max_workers=num_threads)

    def submit_task(self, task, *args, **kwargs):
        return self.executor.submit(task, *args, **kwargs)
