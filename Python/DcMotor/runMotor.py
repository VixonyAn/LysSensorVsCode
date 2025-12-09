import dcMotorStepper as dcStepper

if __name__ == '__main__':
    args = dcStepper._parse_args()
    try:
        stepper = dcStepper.Stepper(args.pins, step_sleep=args.speed, steps_per_rev=args.steps_per_rev)
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