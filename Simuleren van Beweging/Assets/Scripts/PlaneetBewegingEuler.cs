using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlaneetBewegingEuler : MonoBehaviour
{
    public float gConst;

    public Vector3 Force;
    public Vector3 Acceleration;
    public Vector3 Velocity;

    private Rigidbody rb;
    private Rigidbody otherRB;
    public GameObject other;


    void Start()
    {
        // earthMass = 5.97e24f;
        // gConst = 6.67e-11f;
        rb = GetComponent<Rigidbody>();
        otherRB = other.GetComponent<Rigidbody>();

    }

    Vector3 acceleration(Vector3 toMoon, Rigidbody otherRB)
    {
        // Kracht = 1/ r^2
        // Eenheidsvector = vector met lengte 1 -> behoudt richting -> (vec / |vec|)
        return gConst * otherRB.mass / (float)Math.Pow((-toMoon).magnitude, 3) * (-toMoon);
    }

    void FixedUpdate()
    {
        Acceleration = acceleration(transform.position - other.transform.position, otherRB);
        Velocity += Acceleration * Time.deltaTime;
        transform.position += Velocity * Time.deltaTime;
    }
}
