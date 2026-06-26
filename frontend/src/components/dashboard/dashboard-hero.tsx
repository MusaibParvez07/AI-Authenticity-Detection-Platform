export default function DashboardHero() {
  return (
    <section className="relative overflow-hidden rounded-3xl border border-zinc-800 bg-gradient-to-br from-zinc-900 via-zinc-950 to-black p-12">

      {/* Background Glow */}
      <div className="absolute -top-24 -right-24 h-72 w-72 rounded-full bg-blue-500/10 blur-3xl" />

      <div className="absolute -bottom-24 -left-24 h-72 w-72 rounded-full bg-violet-600/10 blur-3xl" />

      {/* Content */}
      <div className="relative z-10">

        {/* Badge */}
        <span className="inline-flex items-center rounded-full border border-blue-500/40 bg-blue-500/10 px-4 py-2 text-sm font-medium text-blue-300">
          AI Powered Detection Platform
        </span>

        {/* Heading */}
        <h1 className="mt-8 text-5xl font-extrabold leading-tight tracking-tight text-white">
          Multi-Modal AI
          <br />
          Fake Detection System
        </h1>

        {/* Description */}
        <p className="mt-6 max-w-3xl text-lg leading-8 text-zinc-300">
          Detect AI-generated images, videos, audio, and text using
          advanced deep learning models with real-time analysis,
          confidence scoring, and forensic intelligence.
        </p>

        {/* Buttons */}
        <div className="mt-10 flex gap-4">

          <button className="rounded-xl bg-blue-600 px-7 py-3 font-semibold text-white transition-all duration-300 hover:bg-blue-700 hover:shadow-lg hover:shadow-blue-500/30">
            Start Detection
          </button>

          <button className="rounded-xl border border-zinc-700 px-7 py-3 font-medium text-white transition-all duration-300 hover:border-zinc-500 hover:bg-zinc-800">
            Learn More
          </button>

        </div>

      </div>

    </section>
  );
}