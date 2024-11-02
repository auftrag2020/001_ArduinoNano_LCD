/*
 * arch_static.h
 *
 *  Created on: 23 Aug 2022
 *      Author: CJU2TR
 */

#ifndef ARCH_STATIC_H_
#define ARCH_STATIC_H_

/**
 * @page staticView Static View
 *
 * The static view describes the BasicSW in terms of layers, components and
 * their interfaces. Based on Autosar, the components are arranged in layers
 * depending on their dependability on the underlying hardware, where the lower
 * layers present a higher dependability.
 *
 * @image html BSW_Layered_Architecture.png "BasicSW Layers" width=750cm
 *
 * Calls from upper to lower layer modules are always done through the public
 * API of the lower level component. Calls from lower to upper modules are always
 * done by means of callbacks, normally implemented as function pointers in the
 * post-build configuration structure passed to the initialization functions of
 * each module.
 *
 * To increase the portability of the BasicSW to different applications, the
 * components can be configured at build time, link-time or post-build time.
 * The user guide and detailed design sections provide more details about
 * component configuration.
 *
 * @section staticViewMCAL MCAL
 *
 * The next figure shows the components at the MCAL layer (drivers). These drivers
 * provide an abstraction from the microcontroller to the upper layers. A detailed
 * description of each driver can be found in the Detailed Design guide.
 *
 * @image html BSW_Architecture-MCAL.png "MCAL drivers" width=750cm
 *
 * @section staticViewECUAL ECUAL
 *
 * The ECU Abstraction Layer (ECUAL) provides an abstraction of the underlying
 * ECU board to the services layer. The ECUAL modules can be classified in several
 * groups according to their functionality:
 *
 *   - I/O
 *   - Communication
 *   - Memory
 *
 * For ECUAL I/O Hardware Abstraction, all external inputs and outputs, both
 * digital and analog, are routed via pins of the microcontroller. If an IO
 * expansor via SPI is used to increase the number of inputs/outputs, the ECUAL
 * I/O module should be extended to access the SPI driver.
 *
 * @image html BSW_Architecture-ECUAL_IO.png "ECUAL - I/O"
 *
 * For ECUAL Memory Abstraction, a Flash EEPROM Emulation module is provided.
 * This module uses the internal data flash of the microcontroller for data
 * storage. If other memory devices should be supported (i.e. an external EEPROM
 * via SPI) this should be implemented in this layer.
 *
 * @image html BSW_Architecture-ECUAL_MEM.png "ECUAL - Memory"
 *
 * For ECUAL Communication Abstraction, a CAN interface module provides an
 * abstraction from the location of the communication controllers on the ECU.
 * This CAN interface uses the CAN controllers in the microcontroller (no external
 * controllers are used).
 *
 * @image html BSW_Architecture-ECUAL_COM.png "ECUAL - Communication"
 *
 * @section staticViewServices Services
 *
 * Services are the highest layer components of the BasicSW. Services can be
 * classified in three groups:
 *
 *   - Memory Services
 *   - Communication Services
 *   - System Services
 *
 * @subsection staticViewMemoryServices Memory Services
 *
 * The NvM Manager is located here. It provides non-volatile data storage using
 * the FEE module in the ECUAL.
 *
 * @image html BSW_Architecture-SVC_MEM.png "Memory Services"
 *
 * @subsection staticViewCommunicationServices Communication Services
 *
 * The communication services consist of multiple modules for signal exchange,
 * network management and diagnostics. Two protocols are supported for diagnostics,
 * UDS and OBD. The implementation of UDS/OBD has been done with flexibility and
 * easy configurability in mind.
 *
 * @image html BSW_Architecture-SVC_COM.png "Communication Services"
 *
 * @subsection staticViewSystemServices System Services
 *
 * System services include the real-time scheduler, timer service, ECU State
 * Manager and Diagnostic Event Manager.
 *
 * @section staticViewRTE RTE
 *
 * The RTE connects the application software components (SWC) with the services
 * in the BasicSW. The RTE must be generated manually for each application project.
 * Currently only Sender-Receiver ports are supported, which are connected by a
 * non-blocking queued channel of length 1.
 */

#endif /* ARCH_STATIC_H_ */
