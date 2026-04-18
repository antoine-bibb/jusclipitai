const plans = [
  {
    name: 'Starter',
    price: '$0',
    detail: 'For experimenting with automated clipping.',
    features: ['3 uploads / month', '30 clip exports', 'Basic captions', '720p render'],
  },
  {
    name: 'Pro',
    price: '$29',
    detail: 'For creators and small teams publishing daily.',
    features: ['30 uploads / month', '150 clip exports', 'Brand templates', '1080p render', 'Priority queue'],
  },
  {
    name: 'Scale',
    price: '$99',
    detail: 'For media teams with heavy publishing cadence.',
    features: ['200 uploads / month', '1000 clip exports', 'Team seats', 'Webhook automations', 'Usage analytics'],
  },
];

export default function PricingPage() {
  return (
    <div className="space-y-8">
      <header className="space-y-3 text-center">
        <span className="badge">Simple pricing</span>
        <h1 className="section-title">Plans for every short-form workflow</h1>
        <p className="mx-auto max-w-2xl text-zinc-300">Start free, then upgrade as your upload volume and export needs increase.</p>
      </header>

      <section className="grid gap-4 md:grid-cols-3">
        {plans.map((plan) => (
          <article key={plan.name} className="card flex flex-col">
            <h2 className="text-2xl font-black text-white">{plan.name}</h2>
            <p className="mt-2 text-4xl font-black text-white">{plan.price}<span className="text-base font-medium text-zinc-400">/mo</span></p>
            <p className="mt-2 text-zinc-300">{plan.detail}</p>
            <ul className="mt-5 space-y-2 text-sm text-zinc-200">
              {plan.features.map((feature) => (
                <li key={feature}>• {feature}</li>
              ))}
            </ul>
            <button className="mt-6 rounded-xl bg-indigo-500 px-4 py-2 font-semibold text-white hover:bg-indigo-400">Choose {plan.name}</button>
          </article>
        ))}
      </section>
    </div>
  );
}
