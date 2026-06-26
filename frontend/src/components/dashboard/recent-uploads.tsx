export default function RecentUploads() {
  return (
    <div className="rounded-3xl border border-white/10 bg-zinc-900 p-8">
      <h2 className="text-2xl font-bold text-white">
        Recent Uploads
      </h2>

      <p className="mt-2 text-zinc-400">
        Your latest AI detection results will appear here.
      </p>

      <div className="mt-8 rounded-2xl border border-dashed border-zinc-700 py-16 text-center">
        <p className="text-lg text-zinc-300">
          No uploads yet
        </p>

        <p className="mt-2 text-zinc-500">
          Upload a file to start AI detection.
        </p>
      </div>
    </div>
  );
}