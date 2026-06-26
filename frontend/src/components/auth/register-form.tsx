"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

import { useAuth } from "@/hooks/use-auth";

export default function RegisterForm() {

  const router = useRouter();

  const { register } = useAuth();

  const [name, setName] =
    useState("");

  const [email, setEmail] =
    useState("");

  const [password, setPassword] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  const [error, setError] =
    useState("");

  async function handleRegister(
    e: React.FormEvent<HTMLFormElement>
  ) {

    e.preventDefault();

    setLoading(true);

    setError("");

    try {

      await register(
        name,
        email,
        password
      );

      router.push("/login");

    } catch (err: any) {

      console.error(err);

      setError(
        err.response?.data?.detail ||
        "Registration failed."
      );

    } finally {

      setLoading(false);

    }

  }

  return (

    <form
      onSubmit={handleRegister}
      className="space-y-6"
    >

      <div>

        <label className="mb-2 block text-sm text-zinc-300">
          Full Name
        </label>

        <Input
          value={name}
          onChange={(e) =>
            setName(e.target.value)
          }
          placeholder="Enter your name"
          required
        />

      </div>

      <div>

        <label className="mb-2 block text-sm text-zinc-300">
          Email
        </label>

        <Input
          type="email"
          value={email}
          onChange={(e) =>
            setEmail(e.target.value)
          }
          placeholder="Enter your email"
          required
        />

      </div>

      <div>

        <label className="mb-2 block text-sm text-zinc-300">
          Password
        </label>

        <Input
          type="password"
          value={password}
          onChange={(e) =>
            setPassword(e.target.value)
          }
          placeholder="Enter your password"
          required
        />

      </div>

      {error && (

        <div className="rounded-xl bg-red-500/10 p-3 text-sm text-red-400">

          {error}

        </div>

      )}

      <Button
        type="submit"
        className="w-full"
        disabled={loading}
      >

        {loading
          ? "Creating Account..."
          : "Create Account"}

      </Button>

    </form>

  );

}