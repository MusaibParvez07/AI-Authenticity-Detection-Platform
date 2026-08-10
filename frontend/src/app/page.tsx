import AppShell from "@/components/layout/app-shell";

import DashboardHero from "@/components/dashboard/dashboard-hero";
import DashboardStats from "@/components/dashboard/dashboard-stats";

import UploadCard from "@/components/upload/upload-card";
import RecentUploads from "@/components/dashboard/recent-uploads";

export default function HomePage() {

  return (

    <AppShell>

      <div className="space-y-8">

        <DashboardHero />

        <DashboardStats />

        <UploadCard />

        <RecentUploads />

      </div>

    </AppShell>

  );

}