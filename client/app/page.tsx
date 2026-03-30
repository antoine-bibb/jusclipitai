import Link from 'next/link';

export default function Home() {
  return (
    <div className="space-y-16">
      <section className="text-center py-16 space-y-6">
        <h1 className="text-5xl font-black">Jus Clip It</h1>
        <p className="text-xl text-zinc-300">Turn long videos into viral clips instantly.</p>
        <div className="flex justify-center gap-4">
          <Link className="px-5 py-3 rounded bg-indigo-500" href="/register">Start Free</Link>
          <Link className="px-5 py-3 rounded border border-zinc-700" href="/pricing">See Pricing</Link>
        </div>
      </section>
      <section className="grid md:grid-cols-3 gap-4">
        {['AI Transcription', 'Story Arc Detection', 'Smart Vertical Reframing'].map((f) => (
          <div key={f} className="card"><h3 className="font-semibold">{f}</h3></div>
        ))}
      </section>
    </div>
  );
}
