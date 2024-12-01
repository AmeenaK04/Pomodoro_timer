import time
from plyer import notification

def pomodoro_timer(work_duration, short_break, long_break, pomodoros_before_long_break):
    count = 0  # Completed pomodoros
    total_elapsed_time = 0  # Total elapsed time in minutes

    print("Pomodoro timer started! Press Ctrl+C to exit.")
    
    try:
        while True:
            # Work session
            print(f"Pomodoro {count + 1}: Focus for {work_duration} minutes.")
            time.sleep(work_duration * 60)
            count += 1
            total_elapsed_time += work_duration
            notification.notify(
                title="Great job!",
                message=f"Pomodoro {count} complete! Take a {short_break} minute break.\n"
                        f"Total time worked: {total_elapsed_time} minutes.",
                timeout=10
            )

            # Short break
            print(f"Take a {short_break}-minute break.")
            time.sleep(short_break * 60)

            # Long break after every set number of pomodoros
            if count % pomodoros_before_long_break == 0:
                print(f"Time for a long break of {long_break} minutes.")
                notification.notify(
                    title="Long Break Time!",
                    message=f"You've completed {pomodoros_before_long_break} pomodoros. Take a {long_break}-minute break.",
                    timeout=10
                )
                time.sleep(long_break * 60)
    except KeyboardInterrupt:
        print("\nTimer stopped. Great work today!")
        notification.notify(
            title="Pomodoro Timer Stopped",
            message=f"You completed {count} pomodoros and worked for {total_elapsed_time} minutes in total.",
            timeout=10
        )

if __name__ == "__main__":
    # Set durations (in minutes)
    work_duration = 25  # Duration of each work session
    short_break = 5     # Duration of each short break
    long_break = 15     # Duration of each long break
    pomodoros_before_long_break = 4  # Number of pomodoros before a long break

    pomodoro_timer(work_duration, short_break, long_break, pomodoros_before_long_break)