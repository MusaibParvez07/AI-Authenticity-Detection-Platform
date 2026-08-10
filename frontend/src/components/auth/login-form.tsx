"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

import { useAuth } from "@/hooks/use-auth";

export default function LoginForm() {

  const router = useRouter();

  const { login } = useAuth();

  const [email, setEmail] = useState("");

  const [password, setPassword] = useState("");

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState("");

  async function handleLogin(
    e: React.FormEvent<HTMLFormElement>
  ) {

    e.preventDefault();

    setLoading(true);

    setError("");

    try {

      await login(
        email,
        password
      );

      // Redirect to Dashboard
      router.push("/dashboard");

    } catch (err) {

      console.error(err);

      setError(
        "Invalid email or password."
      );

    } finally {

      setLoading(false);

    }

  }

  return (

    <form
      onSubmit={handleLogin}
      className="space-y-6"
    >

      {/* Email */}

      <div>

        <label className="mb-2 block text-sm text-zinc-300">

          Email

        </label>

        <Input
          type="email"
          placeholder="Enter your email"
          value={email}
          onChange={(e) =>
            setEmail(e.target.value)
          }
          required
        />

      </div>

      {/* Password */}

      <div>

        <label className="mb-2 block text-sm text-zinc-300">

          Password

        </label>

        <Input
          type="password"
          placeholder="Enter your password"
          value={password}
          onChange={(e) =>
            setPassword(e.target.value)
          }
          required
        />

      </div>

      {/* Error */}

      {error && (

        <div className="rounded-xl bg-red-500/10 p-3 text-sm text-red-400">

          {error}

        </div>

      )}

      {/* Submit */}

      <Button
        type="submit"
        className="w-full"
        disabled={loading}
      >

        {loading
          ? "Signing In..."
          : "Sign In"}

      </Button>

    </form>

  );

}