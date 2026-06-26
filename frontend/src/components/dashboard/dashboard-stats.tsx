import StatCard from "./stat-card";

const stats = [
  {
    title: "Images Scanned",
    value: 1245,
    change: "+12%",
    icon: "🖼️",
  },
  {
    title: "Videos Scanned",
    value: 348,
    change: "+8%",
    icon: "🎥",
  },
  {
    title: "Audio Scanned",
    value: 689,
    change: "+5%",
    icon: "🎤",
  },
  {
    title: "Text Analyzed",
    value: 2019,
    change: "+21%",
    icon: "📄",
  },
];

export default function DashboardStats() {
  return (
    <section className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
      {stats.map((stat) => (
        <StatCard
          key={stat.title}
          stat={stat}
        />
      ))}
    </section>
  );
}