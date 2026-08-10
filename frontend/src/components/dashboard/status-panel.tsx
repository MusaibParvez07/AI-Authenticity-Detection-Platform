"use client";

import {
  Activity,
  BrainCircuit,
  CheckCircle2,
  Database,
  Server,
  ShieldCheck,
} from "lucide-react";

import Card from "@/components/ui/card";
import SectionHeader from "@/components/ui/section-header";

interface SystemStatus {
  backend: string;
  database: string;
  models_loaded: number;
  total_models: number;
  detection_engine: string;
  last_updated: string;
}

interface Props {
  status: SystemStatus;
}

export default function StatusPanel({
  status,
}: Props) {

  const services = [
    {
      title: "Backend API",
      status: status.backend,
      icon: Server,
    },
    {
      title: "Database",
      status: status.database,
      icon: Database,
    },
    {
      title: "AI Models",
      status: `${status.models_loaded}/${status.total_models} Loaded`,
      icon: BrainCircuit,
    },
    {
      title: "Detection Engine",
      status: status.detection_engine,
      icon: ShieldCheck,
    },
  ];

  const platformHealthy =
    status.backend === "Online" &&
    status.database === "Connected" &&
    status.models_loaded === status.total_models &&
    status.detection_engine === "Running";

  return (
    <section className="space-y-6">

      <SectionHeader
        title="Platform Status"
        description="Real-time monitoring of platform services."
      />

      <div className="grid gap-6 xl:grid-cols-[1.4fr_.8fr]">

        {/* Left Card */}

        <Card hover={false}>

          <div className="space-y-4">

            {services.map((service) => {

              const Icon = service.icon;

              return (

                <div
                  key={service.title}
                  className="flex items-center justify-between rounded-2xl border border-white/5 bg-zinc-900/60 p-4"
                >

                  <div className="flex items-center gap-4">

                    <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-gradient-to-br from-violet-600 to-blue-600">

                      <Icon
                        size={22}
                        className="text-white"
                      />

                    </div>

                    <div>

                      <h3 className="font-semibold text-white">
                        {service.title}
                      </h3>

                      <p className="text-sm text-zinc-500">
                        {service.status}
                      </p>

                    </div>

                  </div>

                  <CheckCircle2
                    size={22}
                    className="text-green-500"
                  />

                </div>

              );

            })}

          </div>

        </Card>

        {/* Right Card */}

        <Card
          hover={false}
          glow
          className="flex flex-col justify-between"
        >

          <div>

            <div className="flex items-center gap-4">

              <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-gradient-to-br from-violet-600 to-blue-600">

                <Activity
                  size={28}
                  className="text-white"
                />

              </div>

              <div>

                <h3 className="text-xl font-bold text-white">
                  Platform Health
                </h3>

                <p className="text-sm text-zinc-400">
                  Overall system availability
                </p>

              </div>

            </div>

            <div className="mt-10">

              <h1 className="text-5xl font-black text-green-400">
                {platformHealthy ? "100%" : "75%"}
              </h1>

              <p className="mt-3 text-zinc-400">
                {platformHealthy
                  ? "All services operational"
                  : "Some services require attention"}
              </p>

            </div>

          </div>

          <div className="mt-10 rounded-2xl border border-white/10 bg-zinc-900/70 p-4">

            <p className="text-sm text-zinc-500">
              Last Updated
            </p>

            <p className="mt-1 font-semibold text-white">
              {new Date(
                status.last_updated
              ).toLocaleString()}
            </p>

          </div>

        </Card>

      </div>

    </section>
  );
}