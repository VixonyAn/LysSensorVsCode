import time
import argparse
try:
    import RPi.GPIO as GPIO
except Exception:
    GPIO = None


class Stepper:
    """Controller for a 4-wire ULN2003 stepper (28BYJ-48 style).

    Example:
        s = Stepper([17,18,27,22])
        s.rotate_degrees(90, clockwise=True)
        s.cleanup()
    """

    DEFAULT_SEQUENCE = [
        [1, 0, 0, 1],
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
    ]

    def __init__(self, pins, step_sleep=0.002, steps_per_rev=4096, gpio_module=None):
        """pins: list of 4 BCM pin numbers [in1,in2,in3,in4]
        step_sleep: delay between micro-steps (lower = faster)
        steps_per_rev: number of steps for 360 degrees (default ~4096 for 28BYJ-48)
        gpio_module: optional GPIO module (for testing/mocking)
        """
        self.pins = list(pins)
        self.step_sleep = float(step_sleep)
        self.steps_per_rev = int(steps_per_rev)
        self.sequence = Stepper.DEFAULT_SEQUENCE
        self.seq_len = len(self.sequence)
        self.step_index = 0
        self.GPIO = gpio_module if gpio_module is not None else GPIO
        self._setup_done = False

        if self.GPIO is None:
            raise RuntimeError("RPi.GPIO not available. Run this on a Raspberry Pi or pass a mock gpio_module.")

        self.setup()

    def setup(self):
        if self._setup_done:
            return
        self.GPIO.setmode(self.GPIO.BCM)
        for p in self.pins:
            self.GPIO.setup(p, self.GPIO.OUT)
            self.GPIO.output(p, self.GPIO.LOW)
        self._setup_done = True

    def _set_outputs_for_step(self, idx):
        step = self.sequence[idx]
        for pin, val in zip(self.pins, step):
            self.GPIO.output(pin, GPIO.HIGH if val else GPIO.LOW)

    def step(self, steps, clockwise=True):
        """Move a number of micro-steps. Positive steps move in the selected direction.

        steps: integer micro-steps (not full revolutions). Use rotate_degrees() for degrees.
        clockwise: True for clockwise, False for counter-clockwise
        """
        if not isinstance(steps, int):
            steps = int(steps)

        for _ in range(abs(steps)):
            self._set_outputs_for_step(self.step_index)
            if clockwise:
                self.step_index = (self.step_index - 1) % self.seq_len
            else:
                self.step_index = (self.step_index + 1) % self.seq_len
            time.sleep(self.step_sleep)

    def rotate_degrees(self, degrees, clockwise=True):
        """Rotate approximately `degrees` degrees."""
        steps = int(round((abs(degrees) / 360.0) * self.steps_per_rev))
        self.step(steps, clockwise=clockwise)

    def cleanup(self):
        for p in self.pins:
            try:
                self.GPIO.output(p, self.GPIO.LOW)
            except Exception:
                pass
        try:
            self.GPIO.cleanup()
        except Exception:
            pass


def _parse_args():
    p = argparse.ArgumentParser(description="Control ULN2003 stepper motor on Raspberry Pi")
    p.add_argument("--pins", nargs=4, type=int, default=[17, 18, 27, 22],
                   help="BCM pin numbers for IN1 IN2 IN3 IN4 (default: 17 18 27 22)")
    p.add_argument("--degrees", type=float, default=360.0, help="Degrees to rotate (default 360)")
    p.add_argument("--direction", choices=["cw", "ccw"], default="cw", help="Direction: cw or ccw (default cw)")
    p.add_argument("--speed", type=float, default=0.002, help="Step sleep delay in seconds (lower is faster) default 0.002")
    p.add_argument("--steps-per-rev", type=int, default=4096, help="Micro-steps per 360° (default 4096)")
    return p.parse_args()


if __name__ == '__main__':
    args = _parse_args()
    try:
        stepper = Stepper(args.pins, step_sleep=args.speed, steps_per_rev=args.steps_per_rev)
        clockwise = True if args.direction == 'cw' else False
        print(f"Rotating {args.degrees}° {'clockwise' if clockwise else 'counter-clockwise'} at speed={args.speed}")
        stepper.rotate_degrees(args.degrees, clockwise=clockwise)
    except KeyboardInterrupt:
        print("Interrupted by user")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        try:
            stepper.cleanup()
        except Exception:
            pass