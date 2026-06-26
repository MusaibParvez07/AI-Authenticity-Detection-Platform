import AuthLayout from "@/components/auth/auth-layout";
import AuthCard from "@/components/auth/auth-card";
import LoginForm from "@/components/auth/login-form";

export default function LoginPage() {
  return (
    <AuthLayout
      title="Welcome Back"
      subtitle="Sign in to continue to the AI Fake Detection System."
    >
      <AuthCard>
        <LoginForm />

        <p className="mt-6 text-center text-sm text-zinc-400">
          Don't have an account?{" "}
          <a
            href="/register"
            className="font-medium text-blue-500 hover:text-blue-400"
          >
            Register
          </a>
        </p>
      </AuthCard>
    </AuthLayout>
  );
}