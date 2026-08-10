"use client";

import * as React from "react";
import { Slot } from "@radix-ui/react-slot";
import { cva, type VariantProps } from "class-variance-authority";

import { cn } from "@/lib/utils";

const buttonVariants = cva(
  "inline-flex items-center justify-center rounded-2xl font-semibold transition-all duration-200 disabled:pointer-events-none disabled:opacity-50 focus:outline-none focus:ring-2 focus:ring-violet-500/40",
  {
    variants: {
      variant: {
        default:
          "bg-gradient-to-r from-violet-600 to-blue-600 text-white hover:opacity-90",
        secondary:
          "bg-zinc-900 border border-white/10 text-white hover:bg-zinc-800",
        outline:
          "border border-zinc-700 bg-transparent text-white hover:bg-zinc-900",
        ghost:
          "bg-transparent text-white hover:bg-zinc-900",
        destructive:
          "bg-red-600 text-white hover:bg-red-700",
        success:
          "bg-emerald-600 text-white hover:bg-emerald-700",
      },

      size: {
        sm: "h-9 px-4 text-sm",
        default: "h-11 px-6 text-sm",
        lg: "h-12 px-8 text-base",
        icon: "h-11 w-11",
      },
    },

    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
);

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean;
}

export function Button({
  className,
  variant,
  size,
  asChild = false,
  ...props
}: ButtonProps) {
  const Component = asChild ? Slot : "button";

  return (
    <Component
      className={cn(
        buttonVariants({
          variant,
          size,
        }),
        className
      )}
      {...props}
    />
  );
}

export default Button;