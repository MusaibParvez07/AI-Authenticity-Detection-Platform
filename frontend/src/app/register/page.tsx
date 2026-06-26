import AuthLayout from "@/components/auth/auth-layout";
import AuthCard from "@/components/auth/auth-card";
import RegisterForm from "@/components/auth/register-form";

export default function RegisterPage() {
  return (
    <AuthLayout
      title="Create Account"
      subtitle="Register to access the AI Fake Detection Platform."
    >
      <AuthCard>
        <RegisterForm />

        <p className="mt-6 text-center text-sm text-zinc-400">
          Already have an account?{" "}
          <a
            href="/login"
            className="font-medium text-blue-500 hover:text-blue-400"
          >
            Sign In
          </a>
        </p>
      </AuthCard>
    </AuthLayout>
  );
}