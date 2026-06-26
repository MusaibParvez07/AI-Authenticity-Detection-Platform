interface Props {
  children: React.ReactNode;
}

export default function AuthCard({
  children,
}: Props) {

  return (
    <div className="rounded-3xl border border-zinc-800 bg-zinc-900 p-8 shadow-xl">

      {children}

    </div>
  );
}