import * as React from "react";
import { cn } from "@/lib/utils";

function Input({
  className,
  type,
  ...props
}: React.ComponentProps<"input">) {
  return (
    <input
      type={type}
      data-slot="input"
      className={cn(
        `
        h-12
        w-full
        min-w-0
        rounded-xl
        border
        border-zinc-700
        bg-zinc-900
        px-4
        py-3
        text-base
        text-white
        placeholder:text-zinc-500
        caret-blue-500
        transition-all
        outline-none

        focus:border-blue-500
        focus:ring-2
        focus:ring-blue-500/30

        file:inline-flex
        file:h-6
        file:border-0
        file:bg-transparent
        file:text-sm
        file:font-medium
        file:text-foreground

        disabled:pointer-events-none
        disabled:cursor-not-allowed
        disabled:opacity-50

        aria-invalid:border-red-500
        aria-invalid:ring-2
        aria-invalid:ring-red-500/20
        `,
        className
      )}
      {...props}
    />
  );
}

export { Input };