import { DashboardStat } from "@/types/dashboard";

interface Props {
  stat: DashboardStat;
}

export default function StatCard({ stat }: Props) {
  return (
    <div className="rounded-2xl border border-zinc-800 bg-zinc-900 p-6 transition-all duration-300 hover:border-blue-500/40 hover:bg-zinc-800">

      <div className="flex items-center justify-between">

        <div className="text-3xl">
          {stat.icon}
        </div>

        <span className="rounded-full bg-green-500/10 px-3 py-1 text-sm text-green-400">
          {stat.change}
        </span>

      </div>

      <h3 className="mt-6 text-zinc-400">
        {stat.title}
      </h3>

      <p className="mt-2 text-4xl font-bold text-white">
        {stat.value.toLocaleString()}
      </p>

    </div>
  );
}