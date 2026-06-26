interface AuthLayoutProps {
  title: string;
  subtitle: string;
  children: React.ReactNode;
}

export default function AuthLayout({
  title,
  subtitle,
  children,
}: AuthLayoutProps) {
  return (
    <div className="min-h-screen grid lg:grid-cols-2">

      {/* Left Side */}

      <div className="hidden lg:flex flex-col justify-center bg-gradient-to-br from-blue-700 via-indigo-700 to-violet-900 p-16">

        <h1 className="text-5xl font-bold text-white">
          Multi-Modal AI
        </h1>

        <h2 className="mt-4 text-4xl font-bold text-white">
          Fake Detection System
        </h2>

        <p className="mt-8 max-w-lg text-lg text-blue-100 leading-8">
          Detect AI-generated Images, Videos, Audio and Text using
          state-of-the-art Deep Learning models powered by FastAPI,
          PyTorch and HuggingFace Transformers.
        </p>

        <div className="mt-16 grid grid-cols-2 gap-6">

          <div className="rounded-2xl bg-white/10 p-6 backdrop-blur">
            <h3 className="text-3xl font-bold text-white">
              99%
            </h3>

            <p className="text-blue-100">
              Detection Accuracy
            </p>
          </div>

          <div className="rounded-2xl bg-white/10 p-6 backdrop-blur">
            <h3 className="text-3xl font-bold text-white">
              4
            </h3>

            <p className="text-blue-100">
              AI Models
            </p>
          </div>

        </div>

      </div>

      {/* Right Side */}

      <div className="flex items-center justify-center bg-zinc-950 p-10">

        <div className="w-full max-w-md">

          <h2 className="text-4xl font-bold text-white">
            {title}
          </h2>

          <p className="mt-3 text-zinc-400">
            {subtitle}
          </p>

          <div className="mt-10">

            {children}

          </div>

        </div>

      </div>

    </div>
  );
}