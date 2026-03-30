export default function PricingPage() {
  const plans = [
    { name: 'Free', price: '$0', detail: '5 uploads / 20 clips' },
    { name: 'Pro', price: '$29', detail: '30 uploads / 150 clips' },
    { name: 'Business', price: '$99', detail: '200 uploads / 1000 clips' },
  ];
  return <div className="grid md:grid-cols-3 gap-4">{plans.map((p) => <div key={p.name} className="card"><h2>{p.name}</h2><p>{p.price}/mo</p><p>{p.detail}</p></div>)}</div>;
}
